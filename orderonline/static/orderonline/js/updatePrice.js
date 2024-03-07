window.onload = function() {
    // Get the initial total price from the button's text content
    var button = document.querySelector('.add-to-cart-button');
    var originalText = button.textContent;
    var originalPrice = parseFloat(originalText.replace('Add to Cart ', '').replace(' €', ''));
    var totalPrice = originalPrice;

    // Function to calculate total price
    function calculateTotalPrice() {
        // Reset totalPrice to the original price
        totalPrice = originalPrice;

        // Select all checkbox, radio, and select inputs
        var inputs = document.querySelectorAll('input[type="checkbox"], input[type="radio"]');

        var selectedInputs = document.querySelectorAll('input[type="checkbox"]:checked, input[type="radio"]:checked');
        for (var i = 0; i < selectedInputs.length; i++) {
            totalPrice += parseFloat(selectedInputs[i].dataset.price);
        }

        // Add the price of the selected includeditem
        var selectedIncludedItem = document.querySelector('select[name="included_item"]');
        if (selectedIncludedItem) {
            totalPrice += parseFloat(selectedIncludedItem.options[selectedIncludedItem.selectedIndex].dataset.price);
        }

        // Get the original text without the price
        var originalTextWithoutPrice = originalText.replace(originalPrice.toFixed(2) + ' €', '').trim();

        // Update the button text with the new price
        button.textContent = originalTextWithoutPrice + ' ' + totalPrice.toFixed(2) + ' €';

        // Add change event listener to each input
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('change', calculateTotalPrice);
        }
    }

    // Add change event listener to the includeditem select field
    var includedItemSelect = document.querySelector('select[name="included_item"]');
    if (includedItemSelect) {
        includedItemSelect.addEventListener('change', function() {
            // Reset totalPrice to the original price when the select option changes
            totalPrice = originalPrice;
            calculateTotalPrice();
        });
    }

    // Calculate total price on page load
    calculateTotalPrice();
};