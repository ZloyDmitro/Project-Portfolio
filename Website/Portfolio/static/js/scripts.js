/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function() {
    // Überprüfen, ob die Erfolgsmeldung im lokalen Speicher gespeichert ist
    const successMessage = localStorage.getItem('submitSuccessMessage');

    // Wenn die Erfolgsmeldung im lokalen Speicher vorhanden ist, anzeigen
    if (successMessage) {
        const submitSuccessMessage = document.getElementById('submitSuccessMessage');
        if (submitSuccessMessage) {
            submitSuccessMessage.classList.remove('d-none');
        }

        // Erfolgsmeldung aus dem lokalen Speicher entfernen
        localStorage.removeItem('submitSuccessMessage');
    }

    // Formular absenden
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            // Speichern der Erfolgsmeldung im lokalen Speicher
            localStorage.setItem('submitSuccessMessage', true);
        });
    }
});
