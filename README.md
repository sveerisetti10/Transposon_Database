# Transposon Database

The principle aim of this project is to study the transposon compositions in the genomes of four different species—Takifugu rubripes (ID: 47663), Heterocephalus glaber (10181), Homo sapiens (ID: 9606), and Betta splendens (ID: 158456). The project will involve retrieving RepeatModeler sequences from the UCSC Genome Browser and employing the Repeatmodeler_v2 tool on SCC to locate regions within the genomes of these four distinct species that contain transposon elements. Python scripts will be utilized to parse the multi-FASTA files (generated from RepeatModeler), retrieving sequences that will be structured within a dictionary in which identification numbers serve as keys and sequences serve as values. These sequences will then be organized into different categories based on their respective classifications, including DNA and RNA type (Retro Transposons) and Order of Transposon Type.

ER diagrams explain the relationship between the created databases and connecting the database to the web browser using HTML or CSS. A user interface was created to allow people to interact with the data in the database through queries. Additionally, an AJAX JavaScript script was implemented in the browser to enhance the user experience. The final goal was to use SQL tools to characterize the transposon compositions and see how many transposons might be shared in sequence identity and length and type between the four different species.

