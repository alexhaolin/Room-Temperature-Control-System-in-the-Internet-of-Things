package org.foobar.iot.module8;

import java.util.logging.Logger;
import org.foobar.iot.module8.MqttClientConnector;
import org.foobar.iot.common.ConfigConst;

public class TempActuatorSubscriberApp extends Thread{
	// static
	private static final Logger _Logger = Logger.getLogger(TempActuatorSubscriberApp.class.getName());
	private static TempActuatorSubscriberApp _App;
	
	// parameters
	private MqttClientConnector _mqttClient;
	private String _userName = ConfigConst.DEFAULT_MQTT_USERNAME;
	private String _authToken = ConfigConst.DEFAULT_MQTT_AUTHTOKEN;
	private String _pemFileName = ConfigConst.DEFAULT_MQTT_PEMFILENAME;
	private String _host = ConfigConst.UBIDOTS_HOST;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new TempActuatorSubscriberApp();
		try {
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// constructors
	/**
	 * Default.
	 */

	public TempActuatorSubscriberApp() {
		super();
	}
	
	// public methods
	/**
	 * Connect to the MQTT client, and subscribe to the given topic
	 * unsubscribe the topic after 80s, then disconnect with the MQTT client
	 */
	public void start() {
		_mqttClient = new MqttClientConnector(_host, _userName, _pemFileName, _authToken);
		_mqttClient.connect();
		String topicName = "/v1.6/devices/gatewayforxing/tempactuator";
		_mqttClient.subscribeToTopic(topicName); // subscribe to the given topic
		//_mqttClient.subscribeToAll(); // subscribe all the topic
		try {
			sleep(80000);
			_mqttClient.unSubscribeToTopic(topicName);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		_mqttClient.disconnect();
	}
}
