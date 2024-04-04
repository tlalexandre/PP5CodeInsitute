document.addEventListener('DOMContentLoaded', (event) => {
    let optionsExtrasDataElement = document.getElementById('optionsExtras');
    let parsedOptionsExtras;
    if (optionsExtrasDataElement && optionsExtrasDataElement.textContent.trim() !== "") {
        parsedOptionsExtras = JSON.parse(optionsExtrasDataElement.textContent);
    }

    let form = document.getElementById('id_included_item');


    if (form) {
        form.addEventListener('change', function() {
            let selectedIncludedItem = Number(this.value);
            let optionsExtrasToUse;
            if (optionsExtras instanceof HTMLElement) {
                optionsExtrasToUse = parsedOptionsExtras;
            } else {
                optionsExtrasToUse = optionsExtras;
            }
            if (optionsExtrasToUse && selectedIncludedItem in optionsExtrasToUse) {
                var selectedOptionsExtras = optionsExtrasToUse[selectedIncludedItem];
                if (selectedOptionsExtras) {
                    let optionsExtrasDiv = document.getElementById('options-extras');
                    optionsExtrasDiv.innerHTML = '';
                    let extras = selectedOptionsExtras['Extras'];
                    let options = selectedOptionsExtras['Options'];
                    let extrasTitle = document.createElement('h3');
                    extrasTitle.innerHTML = 'Extras';
                    optionsExtrasDiv.appendChild(extrasTitle);
                    // Create checkboxes for extras
                    for (let i = 0; i < extras.length; i++) {
                        let input = document.createElement('input');
                        input.type = 'checkbox';
                        input.name = 'included_item_extra_' + extras[i].id; // Use the actual ID of the extra
                        input.value = extras[i].id;
                        input.dataset.price = extras[i].price; // Add data-price attribute
                        optionsExtrasDiv.appendChild(input);
                        let label = document.createElement('label');
                        label.innerHTML = extras[i].price == 0 ? extras[i].ingredient__name : extras[i].ingredient__name + " - €" + extras[i].price;
                        optionsExtrasDiv.appendChild(label);
                        optionsExtrasDiv.appendChild(document.createElement('br'));
                    }
                    // Create radio buttons for options
                    for (let optionName in options) {
                        let optionDiv = document.createElement('div');
                        let optionTitle = document.createElement('h3');
                        optionTitle.innerHTML = optionName;
                        optionDiv.appendChild(optionTitle);
                        for (let i = 0; i < options[optionName].length; i++) {
                            let input = document.createElement('input');
                            input.type = 'radio';
                            input.name = 'included_item_option_' + optionName;  // Use optionName as name to ensure only one option can be selected
                            input.value = options[optionName][i].id;
                            input.dataset.price = options[optionName][i].price; // Add data-price attribute
                            // Check if it's the last element in the array
                            if (i === options[optionName].length - 1) {
                                input.checked = true;  // Set the checked property to true
                            }
                            optionDiv.appendChild(input);
                            let label = document.createElement('label');
                            label.innerHTML = options[optionName][i].price == 0 ? options[optionName][i].ingredient__name : options[optionName][i].ingredient__name + " - €" + options[optionName][i].price;
                            optionDiv.appendChild(label);
                            optionDiv.appendChild(document.createElement('br'));
                        }
                        optionsExtrasDiv.appendChild(optionDiv);
                    }
                }
                }
        });
        // Trigger the change event manually
        let event = new Event('change');
        form.dispatchEvent(event);
    }
});

