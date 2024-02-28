## **Análisis del espacio farmacológico de antidepresivos utilizando ciencia de redes**
### **Aplicaciones para el reposicionamiento de fármacos**

Este proyecto consiste en realizar el análisis del espectro de fármacos antidepresivos utilizando farmacología de redes para identificar posibles candidatos al *drug repurposing*. Fue inspirado principalmente por el artículo titulado ["Exploration of the Anti-Inflammatory Drug Space Through Network Pharmacology: Applications for Drug Repurposing"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5838628/) del grupo de investigación del Dr. Guillermo de Anda Jáuregui.

Los objetivos específicos del presente trabajo son:

**1)** Recopilar información sobre los antidepresivos disponibles en bases de datos confiables de acceso público, en concreto, de su estructura química ([PubChem](https://pubchem.ncbi.nlm.nih.gov/)), cambios en los perfiles de expresión génica ante perturbaciones ([LINCS](https://lincsproject.org/)) y reacciones adversas de los fármacos antidepresivos ([SIDER 4.1](http://sideeffects.embl.de/drugs/) y [FAERS](https://open.fda.gov/data/faers/#:~:text=About%20FAERS,drug%20and%20therapeutic%20biologic%20products.)).

**2)** Clasificar a los fármacos antidepresivos en clusters de acuerdo con su a) semejanza estructural y b) semejanza funcional, determinada por matrices de similitud.

**3)** Integrar la información recolectada en redes bipartitas para a) identificar las posibles interacciones funcionales y patológicas con las vías de señalización celulares de los fármacos antidepresivos, mediante el GSEA (análisis de enriquecimiento funcional de genes), b) vincular las reacciones adversas más significativas con los fármacos antidepresivos, a través de medidas estadísticas de frecuencia como el PRR (proportional reporting ratio), y c) realizar la conexión entre cierta perturbación sobre una vía de señalización celular y una reacción adversa derivada de los fármacos antidepresivos, a partir de las redes bipartitas iniciales.

**4)** Estudiar las propiedades topológicas de las redes bipartitas para elegir a los fármacos antidepresivos con alto potencial de reposicionamiento, de acuerdo con un radio favorable entre efectos terapéuticos deseables y tóxicos no deseables.

**5)** Cuantificar el riesgo de posibles reacciones adversas de los antidepresivos tras su reposicionamiento.

#### **Referencias**

> American Psychiatric Association. (2015). Depressive disorders: DSM-5 selections. APP.

> Artigas, F. (2015). Developments in the field of antidepressants, where do we go now?. European Neuropsychopharmacology, 25(5), 657-670.

> Dale, E., Bang-Andersen, B., & Sanchez, C. (2015). Emerging mechanisms and treatments for depression beyond SSRIs and SNRIs. Biochemical pharmacology, 95(2), 81-97.

> Dean, J., & Keshavan, M. (2017). The neurobiology of depression: An integrated view. Asian journal of psychiatry, 27, 101-111.

> De Anda‐Jáuregui, G., McGregor, B. A., Guo, K., & Hur, J. (2019). A Network Pharmacology Approach for the Identification of Common Mechanisms of Drug‐Induced Peripheral Neuropathy. CPT: Pharmacometrics & Systems Pharmacology, 8(4), 211-219.

> De Anda-Jáuregui, G., Guo, K., McGregor, B. A., & Hur, J. (2018). Exploration of the anti-inflammatory drug space through network pharmacology: applications for drug repurposing. Frontiers in Physiology, 9, 151.

> De Anda-Jáuregui, G., Alcalá-Corona, S. A., Espinal-Enríquez, J., & Hernández-Lemus, E. (2019). Functional and transcriptional connectivity of communities in breast cancer co-expression networks. Applied Network Science, 4(1), 1-13.

> Ebada, M. E. (2017). Drug repurposing may generate novel approaches to treating depression. Journal of Pharmacy and Pharmacology, 69(11), 1428-1436.

> Gonda, X., Dome, P., Neill, J. C., & Tarazi, F. I. (2023). Novel antidepressant drugs: Beyond monoamine targets. CNS spectrums, 28(1), 6-15.

> Otte, C., Gold, S. M., Penninx, B. W., Pariante, C. M., Etkin, A., Fava, M., ... & Schatzberg, A. F. (2016). Major depressive disorder. Nature reviews Disease primers, 2(1), 1-20.

> Song, Y., Yang, X., & Yu, B. (2022). Repurposing antidepressants for anticancer drug discovery. Drug discovery today, 27(7), 1924-1935.

> Vogelzangs, N., Duivis, H. E., Beekman, A. T., Kluft, C., Neuteboom, J., Hoogendijk, W., ... & Penninx, B. W. (2012). Association of depressive disorders, depression characteristics and antidepressant medication with inflammation. Translational psychiatry, 2(2), e79-e79.

> Yuan, Z., Chen, Z., Xue, M., Zhang, J., & Leng, L. (2020). Application of antidepressants in depression: a systematic review and meta-analysis. Journal of Clinical Neuroscience, 80, 169-181.
