// JavaScript code for sidebar behavior
const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');
const sideBar = document.querySelector('.sidebar');
const menuBar = document.querySelector('.content nav .bx.bx-menu');
const searchBtn = document.querySelector('.content nav form .form-input button');
const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');

// Set initial sidebar state based on screen width
window.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 768) {
        sideBar.classList.remove('close');
    } else {
        sideBar.classList.add('close');
    }
});

// Handle sidebar link clicks
sideLinks.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', () => {
        sideLinks.forEach(i => {
            i.parentElement.classList.remove('active');
        });
        li.classList.add('active');
    });
});

// Toggle sidebar on menu bar click
menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
});

// Handle search button click
searchBtn.addEventListener('click', function (e) {
    if (window.innerWidth < 576) {
        e.preventDefault();
        searchForm.classList.toggle('show');
        if (searchForm.classList.contains('show')) {
            searchBtnIcon.classList.replace('bx-search', 'bx-x');
        } else {
            searchBtnIcon.classList.replace('bx-x', 'bx-search');
        }
    }
});

// Update sidebar and search form behavior on window resize
window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) {
        sideBar.classList.remove('close');
    } else {
        sideBar.classList.add('close');
    }
    if (window.innerWidth > 576) {
        searchBtnIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
});

//  theme ========== dark =============== light ===============
// JavaScript code for theme toggle
const toggler = document.getElementById('theme-toggle');
const body = document.body;

// Function to set a cookie
function setCookie(name, value, days) {
    const expirationDate = new Date();
    expirationDate.setTime(expirationDate.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + expirationDate.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Function to get a cookie value without redeclaring
function getThemeCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

// Apply the saved theme on page load
document.addEventListener('DOMContentLoaded', function () {
    const savedTheme = getThemeCookie('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark');
        toggler.checked = true;
    }
});

// Handle theme toggle change event
toggler.addEventListener('change', function () {
    if (this.checked) {
        body.classList.add('dark');
        setCookie('theme', 'dark', 180); // 180 days = 6 months
    } else {
        body.classList.remove('dark');
        setCookie('theme', 'light', 180); // 180 days = 6 months
    }
});

