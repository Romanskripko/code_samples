# code_samples
Some experiments and ideas check

# Description

This repo is used for testing some special (and not really special) mechanics.  
Right now you can find here DefaultModelSerializer class (inside the Core module), which is a child of DRF ModelSerializer.  
It has 2 abilities - to extend ModelSerializer's serializer_field_mapping
for custom fields and to build nested serialization without constructions like ```dots = DotsSerializer().```  
You can find examples in default_serializer_examples.
