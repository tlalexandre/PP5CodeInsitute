document.addEventListener('DOMContentLoaded', (event) => {
    let messageModalElement = document.getElementById('messageModal');
    let messageModal = new bootstrap.Modal(messageModalElement, {
        backdrop: 'static',
        keyboard: false
    });

    messageModal.show();

    // Move the modal-backdrop behind the modal
    let modalBackdrop = document.querySelector('.modal-backdrop');
    messageModalElement.parentNode.insertBefore(modalBackdrop, messageModalElement);

    // Close the modal after 5 seconds
    setTimeout(function() {
        messageModal.hide();
    }, 5000);

    // Close the modal when the Close button is clicked
    document.querySelector('#messageModal .btn-close').addEventListener('click', function() {
        messageModal.hide();
    });
    document.querySelector('#messageModal .btn-secondary').addEventListener('click', function() {
        messageModal.hide();
    });
});