package org.haolinxu.iot.module01;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;

public class CoapServerConnection {

	private static final Logger _Logger = 
			Logger.getLogger(CoapServerConnection.class.getName());
	
	private CoapServer _coapServer;
	
	public CoapServerConnection() {
		super();
		
		_coapServer = new CoapServer();
		
		ResourceTemp resourceTemp = new ResourceTemp("myHouseOnTheLake/temp");
		ResourceHumidity resourceHumidity = new ResourceHumidity("myHouseOnTheLake/humidity");
		
		addResouce(resourceTemp);
		addResouce(resourceHumidity);
	}
	
	// public methods
	
	public CoapServerConnection(String ...resourceNames) {
		
	}
	

	
	public void addResouce(CoapResource resource) {
		if (resource != null) {
			_coapServer.start();
		}
	}
	
	public void start() {
		_coapServer.start();
	}
	
	public void stop() {
		_coapServer.stop();
	}
	


}
