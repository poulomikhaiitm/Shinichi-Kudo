from modeller import *
env = environ()
aln = alignment(env)mdl = model(env, file='2h8h', model_segment=('FIRST:A','LAST:A’))
aln.append_model(mdl, align_codes='2h8h', atom_files='tseq1.pdb’)
aln.append(file='qseq1.pir', align_codes='qseq1’)
aln.align2d()
aln.write(file='Q04736-2h8h.ali', alignment_format='PIR')