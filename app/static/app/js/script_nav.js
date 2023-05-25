function toggleNavbar() {
  var header = document.getElementById('header');
  var mobileMenuButton = document.querySelector('.mobile-menu-button');
  
  header.classList.toggle('hidden');
  mobileMenuButton.classList.toggle('hidden');
}
