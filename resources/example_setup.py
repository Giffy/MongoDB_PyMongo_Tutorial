# MongoDB download and installation
!wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-debian71-3.0.15.tgz  # Downloads MongoDB from official repository
!tar xfv mongodb-linux-x86_64-debian71-3.0.15.tgz  >/dev/null                    # Unpack compressed file
!rm mongodb-linux-x86_64-debian71-3.0.15.tgz                                     # Removes downloaded file

# dataset = "https://www.bicing.cat/availability_map/getJsonObject"     # Get JSON file from bicing
dataset = "https://raw.githubusercontent.com/Giffy/MongoDB_PyMongo_Tutorial/master/resources/bicing_data.csv"  
!wget $dataset                                                                   # gets_dataset

# Uploading data to Mongo Database
!mongodb-linux-x86_64-debian71-3.0.15/bin/mongoimport --host brny4kjelauboxl-mongodb.services.clever-cloud.com \
                                                      --port 27017 \
                                                      --username='u1kkdrchfjim80tclysv' \
                                                      --password='FeesC2ACNmI7be61RTst' \
                                                      --db brny4kjelauboxl \
                                                      --collection bicing \
                                                      --type csv\
                                                      --file bicing_data.csv\
                                                      --drop --headerline
