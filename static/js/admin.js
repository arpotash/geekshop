"use strict";

const burger = document.querySelector('.fa-bars');
const leftMenu = document.querySelector('.menu-left');
const closeMenu = document.querySelector('.menu-close');

burger.addEventListener('click', function() {
    leftMenu.classList.add('active');
});

closeMenu.addEventListener('click', function() {
    leftMenu.classList.remove('active');
});