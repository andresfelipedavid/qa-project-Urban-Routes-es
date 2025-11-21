# Urban Routes QA Project

Automatización de pruebas para la plataforma Urban Routes, enfocada en validar funcionalidades clave de la interfaz de usuario y el flujo de pedidos de taxi.

## Tecnologías y técnicas utilizadas

- **Python 3.13**: Lenguaje principal para scripting de pruebas.
- **Selenium WebDriver**: Automatización de interacción con el navegador.
- **Pytest**: Framework de pruebas para estructurar y ejecutar los casos.
- **XPath y CSS Selectors**: Localización precisa de elementos dinámicos.
- **WebDriverWait + Expected Conditions**: Sincronización robusta para elementos cargados dinámicamente.
- **Estructura modular**:
  - `main.py`: contiene los tests automatizados, localizadores y metodos.
  - `data.py`: define datos de prueba reutilizables.
  - `helpers.py`: patrón Page Object para encapsular acciones, funcion retrieve_phone_code
  - `UrbanRoutesPage`: patrón Page Object para encapsular acciones.

## Cómo ejecutar las pruebas

- **Desde el terminal**

pytest main.py > Correr la pruebas en el perfil "pytest in main.py" para que correr todas las pruebas al mismo tiempo

- **Para ver resultados detallados**
- 
pytest -v --tb=short
