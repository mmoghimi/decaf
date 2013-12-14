all:
	thrift --gen py decaf.thrift
	thrift --gen java decaf.thrift
	thrift --gen py:server decaf.thrift
	#cp gen-java/* .
	#javac -cp ".:libthrift-0.9.1.jar:slf4j-jdk14-1.7.5.jar:slf4j-api-1.7.5.jar" decaf.java JavaClient.java

clean:
	rm -r gen-py gen-java *.class