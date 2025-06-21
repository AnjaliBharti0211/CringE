const revealCards = document.querySelectorAll('.product-card');

const options = {
  threshold: 0.2
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('reveal');
      observer.unobserve(entry.target);
    }
  });
}, options);
const products = document.querySelector('.products');

const productsObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      products.classList.add('reveal');
    }
  });
}, { threshold: 0.2 });

productsObserver.observe(products);


revealCards.forEach(card => {
  observer.observe(card);
});
