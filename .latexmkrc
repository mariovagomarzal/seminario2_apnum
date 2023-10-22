# PythonTeX output files
$clean_ext .= " pythontex-files-%R/* pythontex-files-%R";
push @generated_exts, 'pytxcode';

# Beamer fragile frames output files (vrb, nav, snm)
$clean_ext .= " vrb nav snm";

$go_mode = 1;
$pdflatex = "lualatex -interaction=nonstopmode -file-line-error %O %S";
$pdf_mode = 1;
