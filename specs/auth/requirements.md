# Requirements — auth

## R1
CUANDO una persona envíe nombre, correo y contraseña válidos, el sistema DEBE crear una cuenta de usuario.

## R2
SI una persona intenta registrarse con un correo ya registrado ENTONCES el sistema DEBE rechazar la operación con un error de conflicto.

## R3
CUANDO el sistema cree una cuenta, DEBE almacenar la contraseña mediante un hash seguro y NO la contraseña original.

## R4
CUANDO una persona envíe credenciales válidas, el sistema DEBE iniciar sesión y devolver un token JWT.

## R5
SI una persona envía credenciales inválidas ENTONCES el sistema DEBE rechazar el inicio de sesión sin revelar cuál dato fue incorrecto.

## R6
CUANDO una persona use un token JWT válido, el sistema DEBE identificar al usuario autenticado y su rol.

## R7
SI una persona usa un token ausente, inválido o expirado ENTONCES el sistema DEBE rechazar el acceso a endpoints protegidos.

## R8
CUANDO se implementen registro e inicio de sesión, el sistema DEBE tener pruebas unitarias y de integración para los casos exitosos y de error.
