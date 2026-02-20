document.addEventListener('DOMContentLoaded', function () {

  // --- Image Preview Logic ---
  const fileInput = document.getElementById('file-input');
  const previewBox = document.getElementById('preview-box');
  const previewImg = document.getElementById('preview-img');

  if (fileInput) {
    fileInput.addEventListener('change', function (event) {
      const file = event.target.files[0];

      if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
          previewImg.src = e.target.result;
          previewBox.classList.add('active'); // Expands the box
        }

        reader.readAsDataURL(file);
      } else {
        previewBox.classList.remove('active');
        previewImg.src = '';
      }
    });
  }

  // --- Lightbox Modal Logic ---
  const modal = document.getElementById('image-modal');
  const modalImg = document.getElementById('modal-img');
  const closeModal = document.querySelector('.close-modal');
  // Select all images inside the image wrappers
  const taskImages = document.querySelectorAll('.card-image-wrap img');

  if (modal && modalImg) {

    // Open Modal
    taskImages.forEach(img => {
      img.style.cursor = 'zoom-in'; // Enforce pointer

      // Add click listener to the parent wrapper or image itself
      img.parentElement.addEventListener('click', function (e) {
        e.stopPropagation(); // Prevent card clicks if any
        const src = img.getAttribute('src');
        modalImg.src = src;
        modal.classList.add('active');
      });
    });

    // Close Modal via Button
    if (closeModal) {
      closeModal.addEventListener('click', () => {
        modal.classList.remove('active');
        setTimeout(() => { modalImg.src = ''; }, 300); // Clear after transition
      });
    }

    // Close Modal via Overlay Click
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
        setTimeout(() => { modalImg.src = ''; }, 300);
      }
    });

    // Close via Escape Key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        modal.classList.remove('active');
      }
    });
  }
});
