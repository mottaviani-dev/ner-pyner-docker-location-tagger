#Use openjdk as the base image
FROM openjdk:8-jdk-alpine

ENV port=8888 classifierPath=classifiers/english.conll.4class.distsim.crf.ser.gz outputFormat=inlineXML

WORKDIR /home

#Download the english.conll.4class classifier file
RUN wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
RUN unzip stanford-ner-4.2.0.zip

RUN ls -lah ./

WORKDIR /home/stanford-ner-2020-11-17

#Expose port 8888
EXPOSE $port

#Start the NER server
CMD java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer \
    -loadClassifier $classifierPath \
    -port $port -outputFormat $outputFormat