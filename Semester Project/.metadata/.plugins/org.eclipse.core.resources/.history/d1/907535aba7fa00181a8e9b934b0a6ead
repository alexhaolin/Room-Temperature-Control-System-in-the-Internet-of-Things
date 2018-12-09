/**
 * 
 */
package org.foobar.iot.module7;

import java.util.logging.Level;
import java.util.logging.Logger;

import org.foobar.iot.module8.TempActuatorSubscriberApp;

/**
 * @author xingli
 *
 */
public class CoAPServerConnectionApp {
	
	private static final Logger _Logger = 
			Logger.getLogger(CoAPServerConnectionApp.class.getName());
	
	private static CoAPServerConnectionApp _App = null;
	
	/**
	 * default constructor
	 */
	public CoAPServerConnectionApp() {
		super();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			_App = new CoAPServerConnectionApp();
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.SEVERE, "Bad staff ", e);
			System.exit(1);
		}
	}

	//public methods
	
	public void start() {
		TempActuatorSubscriberApp mqttApp = new TempActuatorSubscriberApp();
		mqttApp.start();
		CoAPServerConnection serverConn = new CoAPServerConnection();
		serverConn.start();
	}
}
