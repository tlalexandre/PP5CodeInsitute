const button = document.querySelector('.add-to-cart-button');
const selectedIncludedItem = document.querySelector('select[name="included_item"]');
const quantityInput = $('#id_quantity');

document.addEventListener('DOMContentLoaded', () => {
    // Get the initial total price from the button's text content
    let originalText = button.textContent;
    let originalPrice;

    if (originalText.startsWith('Add to Cart ')) {
        originalPrice = parseFloat(originalText.replace('Add to Cart ', '').replace(' €', ''));
    } else if (originalText.startsWith('Update Item ')) {
        originalPrice = parseFloat(originalText.replace('Update Item ', '').replace(' €', ''));
    }
    let totalPrice = originalPrice;

    console.log("Original Price: ", originalPrice);

    // Function to calculate total price
    function calculateTotalPrice() {
        // Reset totalPrice to the original price
        totalPrice = originalPrice;

        // Select all checkbox, radio, and select inputs
        let inputs = document.querySelectorAll('input[type="checkbox"], input[type="radio"]');

        let selectedInputs = document.querySelectorAll('input[type="checkbox"]:checked, input[type="radio"]:checked');
        for (let i = 0; i < selectedInputs.length; i++) {
            console.log("Selected Input Price: ", selectedInputs[i].dataset.price);
            totalPrice += parseFloat(selectedInputs[i].dataset.price);
        }

        // Add the price of the selected includeditem
        if (selectedIncludedItem) {
            console.log("Selected Included Item Price: ", selectedIncludedItem.options[selectedIncludedItem.selectedIndex].dataset.price);
            totalPrice += parseFloat(selectedIncludedItem.options[selectedIncludedItem.selectedIndex].dataset.price);
        }

        // Get the original text without the price
        let originalTextWithoutPrice = originalText.replace(originalPrice.toFixed(2) + ' €', '').trim();

        // Update the button text with the new price
        button.textContent = originalTextWithoutPrice + ' ' + totalPrice.toFixed(2) + ' €';

        // Add change event listener to each input
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('change', calculateTotalPrice);
        }
    }

    // Add change event listener to the includeditem select field
    let includedItemSelect = document.querySelector('select[name="included_item"]');
    if (includedItemSelect) {
        includedItemSelect.addEventListener('change', function() {
            // Reset totalPrice to the original price when the select option changes
            totalPrice = originalPrice;
            calculateTotalPrice();
        });
    }

    // Calculate total price on page load
    calculateTotalPrice();
});

$(document).ready(function() {

    $('#increase-id_quantity').click(function(event) {
        event.preventDefault();
        let quantity = parseInt(quantityInput.val());
        if (!isNaN(quantity)) {
            quantityInput.val(quantity + 1);
        }
    });

    $('#decrease-id_quantity').click(function(event) {
        event.preventDefault();
        let quantity = parseInt(quantityInput.val());
        if (!isNaN(quantity) && quantity > 1) {
            quantityInput.val(quantity - 1);
        }
    });
});