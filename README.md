# Dropay: Calculadora Financiera
Dropay es una calculadora financiera donde las personas pueden realizar cálculos relacionados con sus créditos de forma fácil y rápida, permitiéndoles almacenar el historial de transacciones para realizarles seguimiento y poder organizar sus finanzas.

- [Set Up](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#set-up)
- [Clases Desarrolladas](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#clases-desarrolladas)
  - [User](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#1-user)
  - [User Credential](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#2-usercredential)
  - [Loan](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#3-loan)
  - [Payment](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#4-payment)
  - [xPayment](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#5-xpayment)
  - [Admin Panel](https://github.com/franco-arroyave/Dropay/tree/RestructureProyect#6-admin-panel)

## Set Up
Para el desarrollo de esta aplicación se uilizó el lenguaje de programación Python y su framework para Desarrollo Web, Django.

A continuación se explica la forma en que se debe configurar el entorno del equipo local para que el proyecto funcione de forma correcta.

### Instala Python
Para la instalación de Python en el equipo, se debe dirigir a la página oficial e instalarlo según el equipo que se esté utilizando. [Clic aquí](https://www.python.org/downloads/)

### Instala Django
Ejecuta el siguiente comando en la consola para instalar Django

`$ python -m pip install Django`

### Hacer migraciones
Con las migraciones se realiza la carga de los modelos en la base de datos.

#### Requisitos
- Se debe tener instalado y ejecutando el servidor de bases de datos. En el caso de este proyecto se utilizó MySQL con XAMPP
- Crear la base de datos y dejarla sin tablas debido a que Django se encarga de crearlas.
- Tener los modelos con la estructura de las tablas. En el caso de este proyecto se crearon los siguientes modelos:
  - [Modelo de Credit](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/models.py), aquí se encuentra toda la información relacionada con las tablas que afectan el módulo Créditos.
  - [Modelo de User](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/models.py), aquí se encuentran los modelos que afectan las tablas del módulo Usuario.

#### Comandos a ejecutar
Antes de ejecutar los siguientes comandos, ubicarse en la carpeta que contiene el proyecto en la consola.
1. `$ python manage.py makemigrations`
2. `$ python manage.py migrate`

### Carga de datos
Después de crear la base de datos, se realiza una carga inicial para añadir algunos registros en las tablas.

1. Revisar los datos en el archivo [fixtures/data.json](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/fixtures/data.json), los cuales van a ser cargados en la base de datos.
2. Ejecutar el siguiente comando en la consola: `$ django-admin loaddata data.json`

## Clases Desarrolladas
### 1. User
#### Crear usuario
Desde el portal de Dropay ya se encuentra habilitada la opción para el registro de nuevos usuarios. Lo anterior se desarrolló utilizando las funciones del modelo `forms` que vienen incluídas con Django.

1. Se realiza el modelado del formulario en el archivo [forms.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/forms.py) con los campos que debe contener para el registro del usuario.
2. Se crea el Templete [signUp.html](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/templates/pages/signUp.html) con la estructura HTML que organiza el formulario de registro.
3. En el archivo [views.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/views.py) se crea la función `def signUp(request):` que se encarga de recibir un request; en caso de que este sea `POST`, se procede a almacenar la información del usuario en la base de datos, en caso contrario, se carga el templete `signUp.html` con el formulario para el registro del usuario.
5. Se añade el path en el archivo [urls.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/urls.py) que dirige al formulario para crear un nuevo registro de usuario: `path('signup', views.signUp, name='signup'),`

![SignUp](https://user-images.githubusercontent.com/78455296/169847885-b727f7e0-63fc-44d4-bbdb-d5651ecd6259.gif)

### 2. UserCredential
El usuario registrado ya puede ingresar a la aplicación con sus credenciales.

- Se añade el `path('', LoginView.as_view(template_name='pages/login.html'), name='login'),` en el archivo [urls.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/urls.py). De esta forma se utiliza el modelo `LoginView` que proporciona Django para la carga de vistas de inicio de sesión; además, se le debe enviar la templete [login.html](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/User/templates/pages/login.html) que contiene la estructura HTML del formulario de Inicio de Sesión.

![SignIn](https://user-images.githubusercontent.com/78455296/169861722-569c5e7f-4390-4fc8-a822-57895f8d96e5.gif)

### 3. Loan
Después de haber iniciado sesión, el usuario puede empezar a calcular y añadir sus creditos.

- Se añaden los paths correspondientes para el proceso de crear y almacenar los créditos en [urls.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/urls.py).
- Se crean los Templetes:
  - [index.html](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/templates/pages/index.html), contiene la estructura de la página de inicio de los créditos. Allí se pueden visualizar los créditos creados y se encuentra el botón para añadir nuevos.
  - [new.html](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/templates/pages/new.html), contiene el formulario con los campos necesarios para poder calcular el crédito.
  - [loanSummary.html](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/templates/pages/loanSummary.html), muestra los resultados obtenidos después de ingresar los datos básicos del crédito. Entre la información calculada se encuentra la cuota que se debe pagar y una grafica que simula el comportamiento de los pagos y el balance del crédito.
- En el archivo [views.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/views.py) se encuentran las funciones que se encargan de cargar los templetes dependiendo de la URL a la que vaya siendo dirigido el usuario.
- En el archivo [loanInfo.py](https://github.com/franco-arroyave/Dropay/blob/RestructureProyect/Credit/loanInfo.py) se realizaron todos los calculos necesarios para el crédito y la grafica. Se tienen funciones como:
  - `def convertInterestRate(self, Period):` que se encarga de convertir la tasa de interés dependiendo de las necesidades de la función que la llama.
  - `def convertPeriod(self):` convierte el plazo ingresado en el periodo de pagos que selecciona el usuario. Por ejemplo, convierte Años en Meses, Semanas o Días.
  - `def monthlyPayment(self):` calcula la cuota que el usuario debe pagar por periodo.

![AddLoan](https://user-images.githubusercontent.com/78455296/169861773-85e15a9d-4e61-4793-979b-4bd472a9807c.gif)

### 4. Payment
> Under construction
### 5. xPayment
> Under construction
### 6. Admin Panel
> Under construction
