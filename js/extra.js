window.MathJax = {
  tex2jax: {
    inlineMath: [ ["$","$"] ],
    displayMath: [ ["$$","$$"] ]
  }
};

$('code').not('.language-python').not('.language-LaTeX').not('.language-plaintext').addClass('nohighlight');

hljs.initHighlightingOnLoad();
