package org.haolinxu.iot.module06;

import java.util.logging.Logger;

public class MqttPubClientTestApp {

	//static
	private static final Logger _pubLogger = 
			Logger.getLogger(MqttSubClientTestApp.class.getName());
	
	private static MqttPubClientTestApp _pubApp;
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_pubApp = new MqttPubClientTestApp();
		
		try {
			_pubApp.start();
			_pubLogger.info("PubClient starts.");
		}catch (Exception E) {
			E.printStackTrace();
		}
	}
	
	//params
	private MqttClientConnector _PubClient;
	
	//contructors
	public  MqttPubClientTestApp() {
		super();
	}
	
	//public methods
	public void start() {
		_PubClient = new MqttClientConnector(null,true);
		
		_PubClient.connect();
		
		String topicName = "test";
		String payload = "This is a test.";
		
		_PubClient.publishMessage(topicName, 2, payload.getBytes());
		
		_PubClient.disconnect();
	}

}
