document.addEventListener('DOMContentLoaded', (event) => {
    var divsWithId = document.querySelectorAll('div[id]');
    // Select all divs with an id

    // Keep track of the currently active nav-link
    var currentActiveNavLink = null;

    var navbar = document.querySelector('.navbar-menu');

    // Create an intersection observer
    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            // Get the nav-link associated with this entry
            var navLink = document.querySelector('a[href="#' + entry.target.id + '"]');

            if (entry.isIntersecting) {
                // If there's a currently active nav-link, remove the classes from it
                if (currentActiveNavLink) {
                    currentActiveNavLink.classList.remove('bg-brand-color', 'white', 'rounded');
                }

                // Add the classes to the new active nav-link
                navLink.classList.add('bg-brand-color', 'white', 'rounded');

                var scrollPos = navLink.offsetLeft - navbar.offsetWidth/2 + navLink.offsetWidth/2;

                navbar.scrollLeft = scrollPos;
                
                // Update the currently active nav-link
                currentActiveNavLink = navLink;
            }
        });
    }, { threshold: 0.2 });  // Adjust the threshold value according to your needs

    // Start observing each div
    divsWithId.forEach(function(div) {
        observer.observe(div);
    });
});

