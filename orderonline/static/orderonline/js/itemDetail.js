document.addEventListener('DOMContentLoaded', (event) => {
    console.log('Script is running');
    var optionsExtrasDataElement = document.getElementById('optionsExtras');
    if (optionsExtrasDataElement) {
        var optionsExtras = JSON.parse(optionsExtrasDataElement.textContent);
        var form = document.getElementById('id_included_item');
        console.log('form:', form);
        if (form) {
            form.addEventListener('change', function() {
                console.log('form change event triggered');
                var selectedIncludedItem = this.value;
                console.log('selectedIncludedItem:', selectedIncludedItem);
                if (selectedIncludedItem in optionsExtras) {
                    var optionsExtrasDiv = document.getElementById('options-extras');
                    optionsExtrasDiv.innerHTML = '';
                    var extras = optionsExtras[selectedIncludedItem]['Extras'];
                    var options = optionsExtras[selectedIncludedItem]['Options'];
                    var extrasTitle = document.createElement('h3');
                    extrasTitle.innerHTML = 'Extras';
                    optionsExtrasDiv.appendChild(extrasTitle);
                    // Create checkboxes for extras
                    for (var i = 0; i < extras.length; i++) {
                        var input = document.createElement('input');
                        input.type = 'checkbox';
                        input.name = 'included_item_extra_' + extras[i].group_id; // Replace 'group_id' with the actual property name 
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
            });
            // Trigger the change event manually
            var event = new Event('change');
            form.dispatchEvent(event);
        }
    } else {
        console.log('optionsExtrasDataElement is null');
    }
});