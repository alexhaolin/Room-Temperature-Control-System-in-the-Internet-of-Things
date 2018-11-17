package org.haolinxu.iot.module07;

import java.util.logging.Logger;

public class CoapClientTestApp {
	
	// static
	private static final Logger _Logger = Logger.getLogger(CoapClientTestApp.class.getName());
	private static CoapClientTestApp _App;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new CoapClientTestApp();
		try {
			_Logger.info("Coap Client starts.");
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// private var's
	private CoapClientConnector _coapClient;

	// constructors
	/**
	*
	*/
	public CoapClientTestApp() {
		super();

	}

	// public methods
	/**
	 * Connect to the CoAP server
	 *
	 */
	public void start() {
		_coapClient = new CoapClientConnector("localhost");
		_Logger.info("Coap Client is testing...");
		_coapClient.runTests("temp");
	}
}
