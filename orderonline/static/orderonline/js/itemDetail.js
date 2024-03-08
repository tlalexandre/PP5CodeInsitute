document.addEventListener('DOMContentLoaded', (event) => {
    var optionsExtrasDataElement = document.getElementById('optionsExtras');
    console.log('optionsExtrasDataElement:', optionsExtrasDataElement);
    console.log('optionsExtrasDataElement.textContent:', optionsExtrasDataElement.textContent);
    var parsedOptionsExtras;
    if (optionsExtrasDataElement && optionsExtrasDataElement.textContent.trim() !== "") {
        parsedOptionsExtras = JSON.parse(optionsExtrasDataElement.textContent);
    }
    console.log('parsedOptionsExtras:', parsedOptionsExtras);
    var form = document.getElementById('id_included_item');
    console.log('form:', form);

    if (form) {
        form.addEventListener('change', function() {
            console.log('form change event triggered');
            var selectedIncludedItem = Number(this.value);
            console.log('selectedIncludedItem:', selectedIncludedItem);
            var optionsExtrasToUse;
            if (optionsExtras instanceof HTMLElement) {
                optionsExtrasToUse = parsedOptionsExtras;
            } else {
                optionsExtrasToUse = optionsExtras;
            }
            if (optionsExtrasToUse && selectedIncludedItem in optionsExtrasToUse) {
                var selectedOptionsExtras = optionsExtrasToUse[selectedIncludedItem];
                if (selectedOptionsExtras) {
                    var optionsExtrasDiv = document.getElementById('options-extras');
                    optionsExtrasDiv.innerHTML = '';
                    var extras = selectedOptionsExtras['Extras'];
                    var options = selectedOptionsExtras['Options'];
                    var extrasTitle = document.createElement('h3');
                    extrasTitle.innerHTML = 'Extras';
                    optionsExtrasDiv.appendChild(extrasTitle);
                    // Create checkboxes for extras
                    for (var i = 0; i < extras.length; i++) {
                        var input = document.createElement('input');
                        input.type = 'checkbox';
                        input.name = 'included_item_extra_' + extras[i].id; // Use the actual ID of the extra
                        input.value = extras[i].id;
                        input.dataset.price = extras[i].price; // Add data-price attribute
                        optionsExtrasDiv.appendChild(input);
                        var label = document.createElement('label');
                        label.innerHTML = extras[i].price == 0 ? extras[i].ingredient__name : extras[i].ingredient__name + " - €" + extras[i].price;
                        optionsExtrasDiv.appendChild(label);
                        optionsExtrasDiv.appendChild(document.createElement('br'));
                    }
                    // Create radio buttons for options
                    for (var optionName in options) {
                        var optionDiv = document.createElement('div');
                        var optionTitle = document.createElement('h3');
                        optionTitle.innerHTML = optionName;
                        optionDiv.appendChild(optionTitle);
                        for (var i = 0; i < options[optionName].length; i++) {
                            var input = document.createElement('input');
                            input.type = 'radio';
                            input.name = 'included_item_option_' + options[optionName][i].id;  // Use optionName as name to ensure only one option can be selected
                            input.value = options[optionName][i].id;
                            input.dataset.price = options[optionName][i].price; // Add data-price attribute
                            optionDiv.appendChild(input);
                            var label = document.createElement('label');
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
        var event = new Event('change');
        form.dispatchEvent(event);
    }
});