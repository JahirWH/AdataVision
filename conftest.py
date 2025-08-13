"""
Configuración de pytest para AdataVision
"""
import pytest
import os
import sys

def pytest_configure(config):
    """Configuración de pytest"""
    # Agregar marcadores personalizados
    config.addinivalue_line(
        "markers", "gui: marks tests that require GUI (skip in CI)"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )

def pytest_collection_modifyitems(config, items):
    """Modificar items de colección de tests"""
    # Saltar tests de GUI en CI
    if os.environ.get('CI') == 'true':
        skip_gui = pytest.mark.skip(reason="Skip GUI tests in CI environment")
        for item in items:
            if "gui" in item.keywords:
                item.add_marker(skip_gui)

@pytest.fixture(scope="session")
def qapp():
    """Fixture para QApplication en tests"""
    if os.environ.get('CI') == 'true':
        # En CI, usar modo offscreen
        os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    
    try:
        from PySide6.QtWidgets import QApplication
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        yield app
    except ImportError:
        pytest.skip("PySide6 not available")
    except Exception as e:
        pytest.skip(f"QApplication not available: {e}")

@pytest.fixture
def temp_file():
    """Fixture para archivos temporales"""
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name
    
    yield temp_path
    
    # Limpiar
    try:
        os.unlink(temp_path)
    except OSError:
        pass 