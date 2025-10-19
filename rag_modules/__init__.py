from .data_preparation import DataPreparationModule
from .index_construction import IndexConstructionModule
from .retrieval_optimization import RetrievalOptimizationModule
from .generation_integration import GenerationIntegrationModule

__all__ = [
    "DataPreparationModule",
    "IndexConstructionModule",
    "RetrievalOptimizationModule",
    "GenerationIntegrationModule",
]

__version__ = "1.0.0"

"""
这个 __init__.py 是包的 “门面”，通过它可以：
让目录被识别为 Python 包；
简化外部导入模块的语法；
明确公共接口和版本信息；
隐藏内部实现细节，提升包的可用性和可维护性。
"""
