package org.haolinxu.iot.module06;

import java.util.logging.Logger;


public class MqttSubClientTestApp
{
	// static
	private static final Logger _subLogger =
		Logger.getLogger(MqttSubClientTestApp.class.getName());
	
	private static MqttSubClientTestApp _subApp;
	/**
	 * @param args
	 */
	public static void main(String[] args){
		_subApp = new MqttSubClientTestApp();
		
		try {
			_subApp.start();
			_subLogger.info("Subclient starts.");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	// params
	private MqttClientConnector _mqttClientConnector;
	
	
	// constructors
	/**
	 * Default.
	 */
	public MqttSubClientTestApp()
	{
		super();
	}
	 
	
	// public methods
	/**
	 * Connect to the MQTT client, then:
	 * 1) If this is the subscribe app, subscribe to the given topic
	 * 2) If this is the publish app, publish a test message to the given topic
	 */
	 
	public void start()
	{
		_mqttClientConnector = new MqttClientConnector();
		
		_mqttClientConnector.connect();
		
		String topicName = "test";
		
		_mqttClientConnector.subscribeToTopic(topicName); // you must implement this method yourself
		//_mqttClientConnector.messageArrived(topic, msg);
		
	
		//_mqttClientConnector.disconnect();
	}
}

