# Grupo 14

Pablo Ormeño 05706/4
Alan Berns 15620/4
diego aguilar 16868/3
Mateo Elizondo 17365/8

## Consideraciones Generales

Para poder acceder a las funcionalidades de la aplicacion existen dos usuarios por defecto, con distintos roles.

### Usuario Administrador

**email:** test@test.com
**contraseña**: 12345

### Usuario Operador

**email:** test2@test2.com
**contraseña:** 12345

## Configuracion

Por defecto, en el mensaje de configuracion se usa 3 palabras claves **USUARIO**, **DISCIPLINA** Y **MONTO**.
Si estan presentes estas palabras, seran reemplazadas segun corresponda con los datos del pago.

Al cambiar el valor base de la cuota, el valor de las cuotas no pagadas, que tengan fecha mayor al mes actual, cambiaran su valor.

## API
Para acceder al login utilizar:

**email:** test@test.com
**contraseña**: 12345

Cuando se envia el token a una api luego de haber iniciado sesion, este se utiliza para identificar al usuario.

**POST /api/me/payment:**
Recibe un arreglo de cuotas y ademas el nombre de la disciplina que se quiere pagar.
Ejemplo:
{
"cuotas": [
{
"month": 1,
"amount": 500
},
{
"month": 2,
"amount": 600
}
],
"disciplina": "Futbol"
}

**POST /api/me/comprobante:**
Recibe ademas del archivo un id de pago, para determinar a que pago se le asoci el comprobante. Requier autorizacion.

Ademas de las API's exigidas existen dos apis complementarias que sirven para realizar un pago.

**GET /api/me/cuotas:**
Permite obtener las cuotas dada una disciplina, requiere autorizacion.

**GET /api/me/disciplines:**
Permite obtener las disciplinas de un socio, requiere autorizacion.
