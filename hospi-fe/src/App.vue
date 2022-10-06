<template>
  <div id="app" class="app">
    <div class="header">
      <h1> HOSPITALIZACION </h1>
        <nav>
        <button v-if="is_auth" v-on:click="loadHome" > Inicio </button>
        <button v-if="is_auth" v-on:click="loadAccount" > Cuenta </button>
        <button v-if="is_auth" v-on:click="logOut" > Cerrar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
        </nav>
      </div>
        <nav class="navbar navbar-expand-lg bg-ligth">
          <div class="container-fluid">
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Dashboard</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Mision</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Vision</a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Seleccione
                  </a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" v-if="is_auth" v-on:click="loadRegistropaciente" >Registrar Paciente</a></li>
                    <li><a class="dropdown-item" href="#">Consultar Paciente</a></li>
                    <li><a class="dropdown-item" href="#">Registrar Medico</a></li>
                    <li><a class="dropdown-item" href="#">Consultar Medico</a></li>
                  </ul>
                  </li>
              </ul>
            </div>
          </div>
        </nav>

      <div class="main-component">
        <router-view
          v-on:completedLogIn="completedLogIn"
          v-on:completedSignUp="completedSignUp"
          v-on:logOut="logOut"
        >
        </router-view>
      </div>

     
      <div class="footer">
        <h2>Misión TIC 2022</h2>
      </div>
      
  </div>
  
</template>
<script>
export default {
  name: 'App',
  data: function(){
    return{
      is_auth: false
  }
 },
 components: {
 },
  methods:{
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;
 
      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "home" });
  },
    loadLogIn: function(){
      this.$router.push({name: "logIn"})
  },
    loadSignUp: function(){
      this.$router.push({name: "signUp"})
  },
    loadHome: function() {
      this.$router.push({ name: "home" });
  },
    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
  },
    loadAccount: function () {
      this.$router.push({ name: "account" });
  },
    loadRegistropaciente: function () {
      this.$router.push({ name: "registropaciente" });
  },
    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },
    completedSignUp: function(data) {
        alert("Registro Exitoso");
        this.completedLogIn(data);
    },
 },
    created: function(){
      this.verifyAuth()
    }
}
</script>
<style>

body{
  margin: 0 0 0 0;
}
.header{
  margin: 0%;
  padding: 0;
  width: 100%;
  min-height: 100px;
  background-color: #4CACBC ;
  color:#E5E7E9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1{
  text-align: center;
}
.header nav{
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button{
  color: #E5E7E9;
  background: #283747;
  border: 1px solid #E5E7E9;
  border-radius: 5px;
  padding: 10px 20px;
}
.header nav button:hover{
  color: #283747;
  background: #E5E7E9;
  border: 1px solid #E5E7E9;
}
.main-component{
  min-height: 80vh;
  margin: 0%;
  padding: 0%;
  background: #FDFEFE;
}
.footer{
  margin:0;
  padding:0;
  width: 100%;
  height: 40px;
  min-height: 100px;
  background-color: #4CACBC;
  color: #E5E7E9;
}
.footer h2{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>