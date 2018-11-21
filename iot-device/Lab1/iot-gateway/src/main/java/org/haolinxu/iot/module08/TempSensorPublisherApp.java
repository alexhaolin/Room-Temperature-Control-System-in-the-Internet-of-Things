package org.haolinxu.iot.module08;

import java.util.logging.Logger;

public class TempSensorPublisherApp {
	private static final Logger _Logger =
			Logger.getLogger(TempSensorPublisherApp.class.getName());
	
	private static TempSensorPublisherApp _pubApp;

	public static void main(String[] args) {
		_pubApp = new TempSensorPublisherApp();
		try {
			_Logger.info("TempSensorPublisherApp starts.");
			_pubApp.start();
		} catch(Exception e) {	
			e.printStackTrace();
		}
	}
	
	// params
	private String host 		= "things.ubidots.com";
	private String userName 	= "A1E-721mX3ls51qGjNW8QS99keo1j3LlHk";
	private String pemFileName  = "C:\\Users\\xuhaolin\\Desktop\\Connected Devices\\iot-device\\Lab1\\ubidots_cert.pem";
	
	private MqttClientConnector _mqttClientConnector;
	
	// constructors
	/**
	 * Default.
	 */
	public TempSensorPublisherApp() {
		super();
	}
	
	// public 
	
	public void start() {
		_mqttClientConnector = new MqttClientConnector(host,
				userName, null, pemFileName);
		
		_mqttClientConnector.connect();
		
		String topic = "/v1.6/devices/alexhandsome/tempsensor";
		String payload = "5";
		
		_mqttClientConnector.publishMessage(topic, 1, payload.getBytes());
		
		_Logger.info("Payload <" + payload + "> sent successfully.");
		
		_mqttClientConnector.disconnect();

		
	}
}
