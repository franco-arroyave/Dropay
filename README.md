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

![AddLoan](https://user-images.githubusercontent.com/78455296/169861773-85e15a9d-4e61-4793-979b-4bd472a9807c.gif)

### 4. Payment
### 5. xPayment
### 6. Admin Panel
