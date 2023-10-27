function toggleSection(sectionId) {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
}
