"""
Code Analyzer Module
Performs static code analysis using AST and various metrics
"""

import ast
from typing import Dict, Any, List
from radon.complexity import cc_visit
from radon.metrics import mi_visit, h_visit
from radon.raw import analyze
import re


class CodeAnalyzer:
    """Analyzes Python code for quality metrics and patterns"""
    
    def __init__(self):
        self.metrics = {}
    
    def analyze(self, code: str) -> Dict[str, Any]:
        """
        Perform comprehensive static analysis on Python code
        
        Args:
            code: Python source code as string
            
        Returns:
            Dictionary containing various code metrics
        """
        try:
            # Parse the code
            tree = ast.parse(code)
            
            # Get basic metrics
            raw_metrics = analyze(code)
            
            # Cyclomatic complexity
            complexity = cc_visit(code)
            avg_complexity = sum(block.complexity for block in complexity) / len(complexity) if complexity else 0
            max_complexity = max((block.complexity for block in complexity), default=0)
            
            # Maintainability index
            mi_score = mi_visit(code, True)
            
            # Halstead metrics
            halstead = h_visit(code)
            
            # AST-based metrics
            ast_metrics = self._analyze_ast(tree)
            
            # Code smells
            smells = self._detect_code_smells(code, tree)
            
            return {
                "lines_of_code": raw_metrics.loc,
                "logical_lines": raw_metrics.lloc,
                "source_lines": raw_metrics.sloc,
                "comments": raw_metrics.comments,
                "blank_lines": raw_metrics.blank,
                "comment_ratio": raw_metrics.comments / raw_metrics.loc if raw_metrics.loc > 0 else 0,
                "avg_complexity": round(avg_complexity, 2),
                "max_complexity": max_complexity,
                "maintainability_index": round(mi_score, 2),
                "halstead_volume": round(halstead.total.volume, 2) if halstead else 0,
                "halstead_difficulty": round(halstead.total.difficulty, 2) if halstead else 0,
                "num_functions": ast_metrics["functions"],
                "num_classes": ast_metrics["classes"],
                "code_smells": smells
            }
        
        except SyntaxError as e:
            return {
                "error": "Syntax error in code",
                "message": str(e),
                "lines_of_code": 0
            }
        except Exception as e:
            return {
                "error": "Analysis error",
                "message": str(e),
                "lines_of_code": 0
            }
    
    def _analyze_ast(self, tree: ast.AST) -> Dict[str, int]:
        """Analyze AST for structural metrics"""
        metrics = {
            "functions": 0,
            "classes": 0,
            "imports": 0,
            "loops": 0,
            "conditionals": 0
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                metrics["functions"] += 1
            elif isinstance(node, ast.ClassDef):
                metrics["classes"] += 1
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                metrics["imports"] += 1
            elif isinstance(node, (ast.For, ast.While)):
                metrics["loops"] += 1
            elif isinstance(node, ast.If):
                metrics["conditionals"] += 1
        
        return metrics
    
    def _detect_code_smells(self, code: str, tree: ast.AST) -> List[str]:
        """Detect common code smells"""
        smells = []
        
        # Long functions (>50 lines)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if hasattr(node, 'end_lineno') and hasattr(node, 'lineno'):
                    func_length = node.end_lineno - node.lineno
                    if func_length > 50:
                        smells.append(f"Long function '{node.name}' ({func_length} lines)")
        
        # Too many parameters
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                num_params = len(node.args.args)
                if num_params > 5:
                    smells.append(f"Function '{node.name}' has too many parameters ({num_params})")
        
        # Deeply nested code
        max_depth = self._get_max_nesting_depth(tree)
        if max_depth > 4:
            smells.append(f"Deeply nested code (depth: {max_depth})")
        
        # Magic numbers
        if re.search(r'\b\d{2,}\b', code):
            smells.append("Magic numbers detected - consider using constants")
        
        return smells
    
    def _get_max_nesting_depth(self, node: ast.AST, depth: int = 0) -> int:
        """Calculate maximum nesting depth"""
        max_depth = depth
        
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.If, ast.For, ast.While, ast.With)):
                child_depth = self._get_max_nesting_depth(child, depth + 1)
                max_depth = max(max_depth, child_depth)
            else:
                child_depth = self._get_max_nesting_depth(child, depth)
                max_depth = max(max_depth, child_depth)
        
        return max_depth
    
    def get_suggestions(self, metrics: Dict[str, Any]) -> List[str]:
        """
        Generate improvement suggestions based on metrics
        
        Args:
            metrics: Analysis results
            
        Returns:
            List of suggestions
        """
        suggestions = []
        
        if "error" in metrics:
            return [f"Fix syntax errors: {metrics.get('message', '')}"]
        
        # Complexity suggestions
        if metrics.get("avg_complexity", 0) > 10:
            suggestions.append("⚠️ High average complexity - consider refactoring complex functions")
        
        if metrics.get("max_complexity", 0) > 15:
            suggestions.append("🔴 Very high maximum complexity - break down complex functions")
        
        # Maintainability
        mi = metrics.get("maintainability_index", 100)
        if mi < 20:
            suggestions.append("🔴 Low maintainability - major refactoring recommended")
        elif mi < 50:
            suggestions.append("⚠️ Moderate maintainability - some refactoring suggested")
        else:
            suggestions.append("✅ Good maintainability!")
        
        # Documentation
        comment_ratio = metrics.get("comment_ratio", 0)
        if comment_ratio < 0.1:
            suggestions.append("📝 Low comment ratio - add more documentation")
        elif comment_ratio > 0.3:
            suggestions.append("✅ Well documented code!")
        
        # Code smells
        smells = metrics.get("code_smells", [])
        if smells:
            suggestions.append(f"🔍 Code smells detected: {len(smells)} issues found")
            suggestions.extend([f"  - {smell}" for smell in smells[:3]])
        
        if not smells and mi > 50:
            suggestions.append("🌟 Clean code! Keep up the good work!")
        
        return suggestions
