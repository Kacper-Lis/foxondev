document.addEventListener('DOMContentLoaded', function() {
    const itemsPerPage = 16;
    const techItems = document.querySelectorAll('.tech-item');
    const totalPages = Math.ceil(techItems.length / itemsPerPage);
    const paginationControls = document.getElementById('pagination-controls');

    function showPage(page) {
        techItems.forEach((item, index) => {
            item.style.display = (index >= (page - 1) * itemsPerPage && index < page * itemsPerPage) ? 'block' : 'none';
        });
    }

    function createPaginationControls() {
        for (let i = 1; i <= totalPages; i++) {
            const li = document.createElement('li');
            li.className = 'page-item';
            if (i === 1) li.classList.add('active');
            li.innerHTML = `<a class="page-link" href="#">${i}</a>`;
            li.addEventListener('click', function(event) {
                event.preventDefault();
                document.querySelectorAll('.page-item').forEach(li => li.classList.remove('active'));
                li.classList.add('active');
                showPage(i);
            });
            paginationControls.appendChild(li);
        }
    }

    showPage(1);
    createPaginationControls();
});
