const divsWithId = document.querySelectorAll('div[id]');
const navLinks = document.querySelectorAll('.navbar-menu a');


document.addEventListener('DOMContentLoaded', (event) => {
    let currentActiveNavLink = null;
    let isUserScrolling = false;
    let isNavLinkClicked = false;  // Flag to indicate whether a navlink was clicked

    let observer = new IntersectionObserver(function(entries) {
        if (isUserScrolling || isNavLinkClicked) return;

        entries.forEach(function(entry) {
            let navLink = document.querySelector('a[href="#' + entry.target.id + '"]');

            if (navLink && entry.isIntersecting) {
                if (currentActiveNavLink) {
                    currentActiveNavLink.classList.remove('bg-brand-color', 'white', 'rounded');
                }

                navLink.classList.add('bg-brand-color', 'white', 'rounded');

                currentActiveNavLink = navLink;
            }
        });
    }, { threshold: 0.15 });

    divsWithId.forEach(function(div) {
        observer.observe(div);
    });


    navLinks.forEach((navLink) => {
        let eventName = 'ontouchend' in window ? 'touchend' : 'click';

        navLink.addEventListener(eventName, function(e) {
            if (e.cancelable){
                e.preventDefault();
            }

            isNavLinkClicked = true;  // Set the flag to true when a navlink is clicked

            // Disconnect the observer
            observer.disconnect();

            let target = document.querySelector(this.getAttribute('href'));
            let title = target.querySelector('h2');  // Change 'h1' to the selector of your title element
            title.scrollIntoView({ behavior: 'smooth', block: 'start' });

            // Reconnect the observer and set the flag back to false after the scroll has completed
            setTimeout(() => {
                divsWithId.forEach(function(div) {
                    observer.observe(div);
                });
                isNavLinkClicked = false;  // Set the flag back to false
            }, 1000);  // Adjust the timeout according to your needs
        });
    });
});