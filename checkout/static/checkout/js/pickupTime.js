document.addEventListener("DOMContentLoaded", function() {
    var now = new Date();
    var minTime = new Date(now.getTime() + 15 * 60 * 1000); // 15 minutes from now

    flatpickr("#id_pickup_time", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        minTime: minTime,
        maxTime: "17:00",
        defaultDate: minTime,
        disable: [
            { from: "00:00", to: "07:00" },
            { from: "17:01", to: "23:59" }
        ]
    });
});