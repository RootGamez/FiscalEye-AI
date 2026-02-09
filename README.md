# AuditSentinel - Auditoría Financiera Inteligente 🔍

## 📋 ¿Qué es AuditSentinel?

**AuditSentinel** es una herramienta de **auditoría financiera automatizada** basada en **Inteligencia Artificial** que detecta anomalías en las transacciones de **cualquier tipo de negocio**: restaurantes, tiendas, consultorios, colegios, agencias, servicios, manufactureras, y más.

### Características principales:

✅ **Carga automática de datos** desde exportaciones de HomeBank  
✅ **Anonimización inteligente** para proteger tu privacidad antes de publicar  
✅ **Detección de anomalías** usando algoritmo Isolation Forest (Machine Learning)  
✅ **Visualización profesional** con gráficos interactivos  
✅ **Análisis temporal** considerando patrones por día de la semana  

### ¿Para qué sirve?

- 🔍 Detectar transacciones sospechosas o errores contables
- 💰 Identificar compras de suministros anormalmente altas
- 📊 Analizar patrones de ingresos y egresos
- 🎯 Generar reportes visuales para auditoría
- 🔐 Publicar datos anonimizados en GitHub sin exponer información real

---

## 🛠️ Instalación Paso a Paso

### Requisitos previos:

- **Python 3.8+** instalado ([descargar aquí](https://www.python.org/downloads/))
- **Git** instalado
- Un archivo CSV exportado desde HomeBank

### Paso 1: Clonar o descargar el proyecto

```bash
# Si tienes acceso al repositorio:
git clone <URL_DEL_REPOSITORIO>
cd FiscalEye-AI

# Si lo descargaste como ZIP:
# Descomprime y abre la terminal en la carpeta
cd FiscalEye-AI
```

### Paso 2: Crear un entorno virtual (Virtual Environment)

El entorno virtual **aísla las librerías** del proyecto para evitar conflictos con otras dependencias.

#### En Windows (PowerShell o CMD):
```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**✅ Éxito:** Verás `(venv)` al inicio de tu terminal.

### Paso 3: Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Las librerías que se instalarán son:
- `pandas` - Manipulación de datos
- `scikit-learn` - Modelos de Machine Learning (Isolation Forest)
- `matplotlib` - Gráficos base
- `seaborn` - Gráficos avanzados

---

## 📂 Estructura del Proyecto

```
FiscalEye-AI/
├── data/
│   ├── raw/                          # 🔒 Tu CSV original (NO se sube a GitHub)
│   │   └── homebank_export.csv       # ← Coloca tu archivo aquí (o cambiar nombre si es diferente)
│   └── processed/
│       └── demo_audit.csv            # CSV anonimizado (seguro subir a GitHub)
├── src/
│   ├── __init__.py
│   ├── data_loader.py                # Carga y limpia el CSV
│   ├── anonymizer.py                 # Anonimiza datos sensibles
│   ├── anomaly_detector.py           # IA: Isolation Forest
│   └── visualizer.py                 # Gráficos con Seaborn
├── outputs/                          # Gráficos generados
├── main.py                           # Script principal (ejecuta todo)
├── requirements.txt                  # Dependencias de Python
├── .gitignore                        # Archivos que NO se suben a GitHub
└── README.md                         # Este archivo
```

---

## 📥 Preparar tus datos

### Opción A: Usando CSV de HomeBank

1. Abre **HomeBank** en tu computadora (u otro software de contabilidad que exporte CSV)
2. Ve a **Archivo → Exportar** (o equivalente en tu software)
3. Selecciona el formato **CSV**
4. Guarda el archivo en: `data/raw/homebank_export.csv`

**Ejemplo de estructura esperada:**
```
Fecha;Pago;Número;Beneficiario;Memo;Importe;Categoría;Etiquetas
2024-01-15;Transferencia;001;Proveedor XYZ;Compra insumos;-150.50;Suministros;Compra
2024-01-15;Depósito;002;Cliente ABC;Venta;250.00;Ingresos;Venta
```

**Válido para cualquier negocio**, cambios los beneficiarios según tu caso.

### Opción B: CSV con nombre diferente

Si tu CSV tiene **otro nombre** (ej: `pizzeria_2024.csv`):

1. Edita el archivo `main.py`
2. Busca esta línea:
   ```python
   raw_path = os.path.join("data", "raw", "homebank_export.csv")
   ```
3. Cámbiala por:
   ```python
   raw_path = os.path.join("data", "raw", "pizzeria_2024.csv")
   ```
4. Guarda el archivo

### Columnas requeridas en tu CSV:

| Columna | Tipo | Ejemplo | Obligatoria |
|---------|------|---------|-------------|
| `Fecha` | Texto (YYYY-MM-DD) | 2024-01-15 | ✅ Sí |
| `Importe` | Número (con . o ,) | -150.50 o 250,00 | ✅ Sí |
| `Beneficiario` | Texto | Sabor Llanero | ✅ Sí |
| `Categoría` | Texto | Suministros | ❌ Opcional |
| `Memo` | Texto | Compra ingredientes | ❌ Opcional |

---

## 🚀 Ejecutar el programa

### Paso 1: Asegúrate de que el venv está activo

```bash
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### Paso 2: Verifica que tu CSV esté en `data/raw/`

```bash
# Verifica que existe:
ls data/raw/
# Debe aparecer: homebank_export.csv (o el nombre que uses)
```

### Paso 3: Ejecuta el script principal

```bash
python main.py
```

### ¿Qué sucede ahora? 🔄

1. ✅ Lee tu CSV desde `data/raw/homebank_export.csv` (o el archivo que configuraste)
2. ✅ **Limpia y normaliza** los datos (fechas, números, espacios)
3. ✅ Anonimiza los datos (cambia montos, beneficiarios, fechas)
4. ✅ Exporta CSV anonimizado a `data/processed/demo_audit.csv`
5. ✅ Entrena el modelo de Machine Learning (Isolation Forest)
6. ✅ Detecta anomalías usando patrón de **monto + día de la semana**
7. ✅ **Imprime en consola las 5 anomalías más grandes**
8. ✅ Genera un gráfico profesional en `outputs/audit_scatter.png`

### Ejemplo de salida en consola:

```
Top 5 anomalies by amount:
    Fecha Importe Tipo   Beneficiario anomaly
0 2024-05-20 -5000.00 Egreso Proveedor_Suministros -1
1 2024-06-15 -3500.00 Egreso Proveedor_Suministros -1
2 2024-07-02 2800.00 Ingreso Venta_Publico -1
...
Saved plot to outputs/audit_scatter.png
```

---

## 📊 Resultados

### 1. Gráfico de Auditoría

Se genera un archivo PNG en `outputs/audit_scatter.png` que muestra:

- **Eje X:** Fechas de las transacciones
- **Eje Y:** Montos (en la moneda de tu negocio: pesos, euros, dólares, etc.)
- 🟢 **Puntos verdes:** Transacciones normales
- 🔴 **Puntos rojos:** Anomalías detectadas (⚠️ revisar estos casos)
- **Línea gris horizontal en 0:** Separación visual Ingresos (arriba) vs Egresos (abajo)

**¿Cómo interpretar?**
- Puntos rojos muy altos/bajos = Transacciones fuera de lo normal → Posibles errores, fraudes o gastos excepcionales
- Clusters de puntos = Patrones normales de tu negocio
- Cambios bruscos = Variaciones estacionales o eventos especiales

### 2. CSV Anonimizado

Se crea `data/processed/demo_audit.csv` con datos modificados:

- **Montos:** ±10% aleatorio (mantiene tendencias pero cambia cifras exactas)
- **Beneficiarios:** Genéricos (Proveedor_XXXX, Cliente_YYYY)
- **Fechas:** ±3 días (no coincide exactamente con tus libros reales)

**✅ Seguro para publicar en GitHub sin exponer datos confidenciales**

Este archivo sirve como:
- Demo para mostrar a otros desarrolladores
- Pruebas automatizadas
- Documentación de casos de uso

---

## 🔧 Configuración avanzada

### Cambiar el nivel de sensibilidad

En `main.py`, línea con `FinancialAnomalyDetector`:

```python
detector = FinancialAnomalyDetector(contamination=0.05)  # 5% son anomalías
```

- **0.01** = Muy estricto (detecta pocas anomalías, mejor para empresas grandes)
- **0.05** = **Recomendado** (5% por defecto, equilibrio)
- **0.10** = Menos sensible (detecta más casos, mejor para negocios pequeños o caóticos)

**Experimento:** Ajusta según tu negocio. Si detecta muchas falsas anomalías, aumenta a 0.10. Si pasa algo sin detectar, baja a 0.01.

### Cambiar la carpeta de salida

En `src/visualizer.py` o `main.py`, modifica:

```python
plot_path = plot_audit_results(labeled_df, output_dir="outputs")
```

Por:

```python
plot_path = plot_audit_results(labeled_df, output_dir="reportes")
```

---

## 🐛 Solución de problemas


### ❌ Error: "FileNotFoundError: data/raw/homebank_export.csv"

**Solución:**
1. Verifica que el archivo esté en `data/raw/`
2. Verifica el nombre exacto del archivo
3. Cambia el nombre en `main.py` si es necesario

### ❌ Error: "ModuleNotFoundError" o módulos faltantes

**Solución:**
```bash
# Desactiva el venv
deactivate

# Vuelve a crear uno limpio
python -m venv venv
venv\Scripts\activate  # en Windows

# Reinstala todo
pip install -r requirements.txt
```



## 📖 Estructura de datos internamente

### Transformación de datos (Pipeline de Datos)

El programa automáticamente:

1. **Lee CSV con separador `;`** (formato HomeBank / estándar)
2. **Convierte fechas** al formato YYYY-MM-DD
3. **Limpia montos** (detecta comas, puntos, números negativos)
4. **Crea nuevas columnas automáticas:**
   - `Tipo`: "Ingreso" (>0) o "Egreso" (<0)
   - `Monto_Abs`: Valor absoluto para análisis
   - `Dia_Semana`: 0 (lunes) a 6 (domingo) *patrón semanal importante en negocios*
   - `anomaly`: -1 si es anomalía, 1 si es normal

### Algoritmo: Isolation Forest 🤖

**¿Cómo funciona?**

Este algoritmo de **Machine Learning sin supervisión** aísla puntos anómalos:

1. Divide el espacio de datos recursivamente
2. Los puntos raros se aíslan rápidamente (anomalías)
3. Los puntos normales necesitan más divisiones

**Características que analiza:**
- **Monto_Abs** (¿muy alto o muy bajo?)
- **Dia_Semana** (¿inusual para este día?)

**Ejemplo práctico:**
- Lunes: Gasto de $500 en suministros = NORMAL
- Domingo: Gasto de $5000 en suministros = ANOMALÍA (¿Por qué comprar un domingo?)
- Cualquier día: Venta de $10 = NORMAL
- Cualquier día: Venta de $0.50 = ANOMALÍA (¿Venta tan pequeña?)

**Sensibilidad:** Marca el 5% más inusual (configurable en `main.py`)

---

## 🔐 Privacidad y GitHub

### ✅ Safe to commit ✅
- `data/processed/demo_audit.csv` (datos anonimizados)
- `outputs/*.png` (gráficos de demostración)
- Código fuente

### ❌ NEVER commit ❌
- `data/raw/` (tus CSVs originales con datos reales)
- Cualquier archivo con información confidencial

**El `.gitignore` ya protege `data/raw/` automáticamente.**

---

## � Casos de uso reales

### Por tipo de negocio:

| Negocio | Qué detecta | Beneficio |
|---------|-----------|----------|
| **Restaurante** | Compras de proveedores inusualmente altas un lunes | Detectar errores o sobrefacturación |
| **Tienda** | Ventas anormalmente bajas un fin de semana | Revisar operaciones |
| **Consultorio** | Pago a proveedor a una hora rara | Posible fraude |
| **Colegio** | Ingresos de matriculas fuera de fechas normales | Controlar dinámica financiera |
| **Agencia** | Gastos que no coinciden con proyectos | Auditoria interna |
| **Garage** | Compra de repuestos muy grande | Revisar si es real o error |



## 📄 Licencia

Este proyecto es **código abierto**. Úsalo libremente en tu negocio.

---

## 🤝 Contribuir

¿Encontraste un bug? ¿Tienes una mejora?

1. Fork el repositorio
2. Crea tu rama: `git checkout -b feature/tu-feature`
3. Commit tus cambios: `git commit -m "Agrega tu feature"`
4. Push: `git push origin feature/tu-feature`
5. Abre un Pull Request

---

## 📝 Notas importantes

1. **Backup primero:** Guarda una copia de tu CSV original antes de experimentar
2. **Datos anonimizados:** Los archivos en `data/processed/` son seguros para publicar
3. **Reestablecer el proyecto:**
   ```bash
   rm -r venv
   git clean -fd
   git reset --hard
   ```

---

**¡Gracias por usar FiscalEye-IA! 🚀**

Para preguntas o reportar problemas, contacta al equipo de desarrollo.
