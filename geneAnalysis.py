from __future__ import division;
import Bio;
from Bio.Seq import Seq;
from Bio.Alphabet import IUPAC;
import matplotlib.pyplot as plt;
import bokeh;
import seaborn as sns;
from Bio.Data import CodonTable
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np;
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
finDna=[];
finStr='';
#dpl=DNARenderer();
inpt='GACTCGGGGTGCCCTTCTGCGTGAAGGCTGAGAAATACCCGTATCACCTGATCTGGATAATGCCAGCGTAGGGAAGTT';
inpt=inpt.upper();
Acnt,Gcnt,Tcnt,Ccnt=0,0,0,0;
Acnt=inpt.count('A');
Gcnt=inpt.count('G');
Tcnt=inpt.count('T');
Ccnt=inpt.count('C');
GCPcnt=((Gcnt+Ccnt)/(Acnt+Gcnt+Tcnt+Ccnt));
print GCPcnt
x=['A','G','T','C','GCCount'];
y=[Acnt,Gcnt,Tcnt,Ccnt,GCPcnt];
sns.axes_style('white')
sns.set_style('white')
ax = sns.barplot(x, y)
mysq=Seq(inpt,IUPAC.unambiguous_dna);
print mysq.alphabet;
mysq1=[mysq[i:i+3] for i in range(0, len(mysq), 3)]
mRna=mysq.transcribe();
print mRna;
mRna=[mRna[i:i+3] for i in range(0, len(mRna), 3)]
for i in mRna:
	finDna.append(i.translate());
	finStr+=str(i.translate())
print "the number of codons is %s" %(str(len(mysq1)));
'''
print finDna;
print standard_table;
print mito_table
#finDna=mRna.translate();
#print finDna;
features1=[
    GraphicFeature(start=0, end=200, strand=+1, color="#ffd700",
                   label=mysq1[0]),
    GraphicFeature(start=200, end=400, strand=+1, color="#ffcccc",
                   label=mysq1[1]),
    GraphicFeature(start=400, end=600, strand=-1, color="#cffccc",
                   label=mysq1[2]),
    GraphicFeature(start=600, end=800, strand=+1, color="#ccccff",
                   label=mysq1[3])
]
features2=[
    GraphicFeature(start=0, end=200, strand=+1, color="#ffd700",
                   label=mRna[0]),
    GraphicFeature(start=200, end=400, strand=+1, color="#ffcccc",
                   label=mRna[1]),
    GraphicFeature(start=400, end=600, strand=-1, color="#cffccc",
                   label=mRna[2]),
    GraphicFeature(start=600, end=800, strand=+1, color="#ccccff",
                   label=mRna[3])
]
features3=[
    GraphicFeature(start=0, end=200, strand=+1, color="#ffd700",
                   label=finDna[0]),
    GraphicFeature(start=200, end=400, strand=+1, color="#ffcccc",
                   label=finDna[1]),
    GraphicFeature(start=400, end=600, strand=-1, color="#cffccc",
                   label=finDna[2]),
    GraphicFeature(start=600, end=800, strand=+1, color="#ccccff",
                   label=finDna[3])
]
AminoAcid=''.join(finStr);
analysed_seq = ProteinAnalysis(AminoAcid);
molwt=analysed_seq.molecular_weight()
gravyweight=analysed_seq.gravy()
x1=['molWt','Gravy'];
y1=[molwt,gravyweight]
#ax1=sns.barplot(x1,y1);
aaccnt=analysed_seq.count_amino_acids()
aroma=analysed_seq.aromaticity();
isoEle=analysed_seq.isoelectric_point();
flex=analysed_seq.flexibility();
insta=analysed_seq.instability_index();
print aaccnt,isoEle,aroma,insta;
secfun=analysed_seq.secondary_structure_fraction();
print secfun;
record = GraphicRecord(sequence_length=800, features=features1);
rec2=GraphicRecord(sequence_length=800, features=features2);
rec3=GraphicRecord(sequence_length=800, features=features3);
'''
ax.set_yticks([10,20,30,40,50,60,70,80,90])
ax.set_xticklabels(x);
#ax.set_xticks(y1);
#ax1.set_yticks([1000,2000,3000,4000,5000]);
#ax1.set_xticklabels(x1);
#record.plot();
#rec2.plot();
#rec3.plot();
print Acnt,Gcnt,Tcnt,Ccnt
#ATOM      1  N   LEU A 125       4.329 -12.012   2.376  1.00  0.00           N

#ATOM     29  P     G A  11     -24.416  -5.829  71.866  1.00 76.40           P
plt.show();
