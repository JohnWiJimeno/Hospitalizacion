<template>
            <div class="container d-flex justify-content-center align-center">
                <form class="w-50">
                <h2 class="text-center mb-4">Registro de Pacientes</h2>
                <hr>
                    <div class="mb-2">
                        <label for="exampleInputEmail1" class="form-label">ID Paciente</label>
                        <input type="number" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    </div>
                    <div class="mb-2">
                        <label for="inputNombre" class="form-label">Nombre</label>
                        <input type="text" class="form-control" id="inputNombre">
                    </div>
                    <div class="mb-2">
                        <label for="inputApellidos" class="form-label">Apellidos</label>
                        <input type="text" class="form-control" id="inputApellidos">
                    </div>
                    <div class="mb-2">
                        <label for="inputCiudad" class="form-label">Ciudad</label>
                        <input type="text" class="form-control" id="inputCiudad">
                    </div>
                    <div class="mb-2">
                        <label for="inputDireccion" class="form-label">Direccion</label>
                        <input type="text" class="form-control" id="inputDireccion">
                    </div>
                    <div class="mb-2">
                        <label for="inputFechan" class="form-label">Fecha de Nacimiento</label>
                        <input type="date" class="form-control" id="inputFechan">
                    </div>
                    <div class="mb-2">
                        <label for="inputLatitud" class="form-label">Latitud</label>
                        <input type="text" class="form-control" id="inputLatitud">
                    </div>
                    <div class="mb-2">
                        <label for="inputLongitud" class="form-label">Longitud</label>
                        <input type="text" class="form-control" id="inputLongitud">
                    </div>
                     <div class="mb-2">
                        <label for="inputEmail" class="form-label">Email</label>
                        <input type="email" class="form-control" id="inputEmail">
                    </div>
                    <div class="mb-2">
                        <label for="inputidauxiliar" class="form-label">ID Auxiliar</label>
                        <input type="number" class="form-control" id="inputidauxiliar">
                    </div>
                    <div class="mb-2">
                        <label for="inputidenfermero" class="form-label">ID Enfermero</label>
                        <input type="number" class="form-control" id="inputidenfermero">
                    </div>
                    <div class="mb-2">
                        <label for="inputidfamiliar" class="form-label">ID Familiar</label>
                        <input type="number" class="form-control" id="inputidfamiliar">
                    </div>
                    <div class="mb-2">
                        <label for="inputidmedico" class="form-label">ID Medico</label>
                        <input type="number" class="form-control" id="inputidmedico">
                    </div>
                    <div class="mb-2">
                        <label for="inputiduser" class="form-label">ID Usuario</label>
                        <input type="number" class="form-control" id="inputiduser">
                    </div>
                    <div class="d-flex justify-content-center pt-3">
                        <button type="submit" class="btn btn-primary">Registrar</button>
                    </div>
                </form>
            </div>
</template>
<script>

</script>
<style>
.container{
    padding: 25px;
}
.btn{
    border-radius: 40px;
    width: 300px    
}
</style>