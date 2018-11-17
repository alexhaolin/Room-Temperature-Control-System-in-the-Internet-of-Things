package org.haolinxu.iot.module07;

import java.util.logging.Logger;

public class CoapServerTestApp {
	
	// static
	private static final Logger _Logger = Logger.getLogger(CoapServerTestApp.class.getName());
	private static CoapServerTestApp _App;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new CoapServerTestApp();
		try {
			_Logger.info("Coap Server starts.");
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// private var's
	private CoapServerConnector _coapServer;

	// constructors
	/**
	*
	*/
	public CoapServerTestApp() {
		super();
	}

	// public methods
	/**
	*
	*/
	public void start() {
		_coapServer = new CoapServerConnector();
		_coapServer.start();
	}
}
