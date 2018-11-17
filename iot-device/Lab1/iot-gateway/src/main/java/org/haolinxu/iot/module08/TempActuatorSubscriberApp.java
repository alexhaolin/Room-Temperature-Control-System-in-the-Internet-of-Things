package org.haolinxu.iot.module08;

import java.util.logging.Logger;

public class TempActuatorSubscriberApp {
	
	// static
	private static final Logger _Logger =
			Logger.getLogger(TempActuatorSubscriberApp.class.getName());
	
	private static TempActuatorSubscriberApp _actApp;

	public static void main(String[] args) {
		_actApp = new TempActuatorSubscriberApp();
		try {
			_Logger.info("Actuator starts.");
			_actApp.start();
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
	public TempActuatorSubscriberApp() {
		super();
	}
	
	// public 
	
	public void start() {
		_mqttClientConnector = new MqttClientConnector(host,
				userName,null, pemFileName);
		
		_mqttClientConnector.connect();
		
		String topic = "/v1.6/devices/alexhandsome/tempactuator";
		
		_mqttClientConnector.subscribeToTopic(topic);
		
		_mqttClientConnector.disconnect();
		
		
	}

}