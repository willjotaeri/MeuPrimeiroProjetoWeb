const passwordInput = document.getElementById("id_password");
const showPasswordIcon = document.querySelector(".show-password-icon");

showPasswordIcon.addEventListener("click", function() {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPasswordIcon.classList.remove("fa-eye-slash");
    showPasswordIcon.classList.add("fa-eye");
  } else {
    passwordInput.type = "password";
    showPasswordIcon.classList.remove("fa-eye");
    showPasswordIcon.classList.add("fa-eye-slash");
  }
});

// Ao marcar a opção "Lembrar senha"
document.getElementById("lembrarSenhaCheckbox").addEventListener("change", function() {
  var username = document.getElementById("id_username").value;
  var password = document.getElementById("id_password").value;
  
  if (this.checked) {
    // Armazenar usuário e senha em cookies
    document.cookie = "username=" + username + "; path=/";
    document.cookie = "password=" + password + "; path=/";
  } else {
    // Limpar cookies de usuário e senha
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
    document.cookie = "password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
  }
});

// Função para definir os cookies de usuário e senha
function setRememberedCredentials() {
  var username = document.getElementById("id_username").value;
  var password = document.getElementById("id_password").value;

  // Definir os cookies com um tempo de expiração de 30 dias
  setCookie("username", username, "9999-12-31");
  setCookie("password", password, "9999-12-31");
}

// Função para definir um cookie com tempo de expiração
function setCookie(name, value, days) {
  var expires = "";

  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/";
}

// Função para verificar se os cookies de usuário e senha existem
function checkRememberedCredentials() {
  var usernameCookie = getCookie("username");
  var passwordCookie = getCookie("password");

  // Verificar se os cookies existem e preencher os campos de login
  if (usernameCookie && passwordCookie) {
    document.getElementById("id_username").value = usernameCookie;
    document.getElementById("id_password").value = passwordCookie;
    document.getElementById("lembrarSenhaCheckbox").checked = true;
  }
}

// Função para obter o valor de um cookie
function getCookie(name) {
  var cookieValue = "";
  var cookies = document.cookie.split(";");

  for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    if (cookie.substring(0, name.length + 1) === name + "=") {
      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
      break;
    }
  }

  return cookieValue;
}

// Evento de carregamento da página
window.addEventListener("load", function() {
  checkRememberedCredentials();
});

function redirectToHome() {
  $.ajax({
    url: '/home_solicitante/', // URL do endpoint que lida com a solicitação
    type: 'GET',
    success: function(response) {
      window.location.href = '/home_solicitante/'; // Redirecionar para a página desejada
    },
    error: function(error) {
      console.log('Ocorreu um erro ao processar a solicitação.');
    }
  });
  return false; // Para evitar o comportamento padrão do clique no elemento
}

