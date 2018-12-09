/**
 * 
 */
package org.foobar.iot.module7;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;
import org.foobar.iot.common.ConfigConst;

/**
 * @author xingli
 *
 */
public class CoAPServerConnection {

	//static
	private static final Logger _Logger = 
			Logger.getLogger(CoAPServerConnection.class.getName());
	
	
	// private var's
	private CoapServer _coapServer;
	private String _protocol;
	private String _host;
	private int _port;
	private CoapClient _clientConn;
	private String _serverAddr;
	
	/**
	 * Default constructor
	 */
	public CoAPServerConnection() {
		this(null);
	}
	

	/**
	 * Constructor
	 * @param host: The name of the broker to connect.
	 */
	public CoAPServerConnection(String host) {
		super();
		_protocol = ConfigConst.DEFAULT_COAP_PROTOCOL;
		_port = ConfigConst.DEFAULT_COAP_PORT;
		if (host != null && host.trim().length() > 0) {
			_host = host;
		} else {
			_host = ConfigConst.DEFAULT_COAP_SERVER;
		}		
		initServer();
	}
	
	//public methods
	/**
	 * initiate the server and add resources to the server
	 */
	public void initServer() {
		_coapServer = new CoapServer();
		ResourceTemp resourceTemp = new ResourceTemp("temp");
		ResourceHumidity resourceHumidity = new ResourceHumidity("humidity");
		addResource(resourceTemp);
		addResource(resourceHumidity);
	}
	
	public void addDefaultResource(String Name) {
		
	}
	
	/**
	 * 
	 * @param resource: the CoapResource that to be added to coap server
	 */
	public void addResource(CoapResource resource) {
		if (resource != null) {
			if (_coapServer != null) {			
				_coapServer.add(resource);
			}
		}
	}
	
	/**
	 * Start a COAP server
	 */
	public void start() {
		if (_coapServer == null) {
			_Logger.info("Creating CoAP server instance and 'temp' handler...");
			initServer();
		}
		_Logger.info("Starting CoAP server...");
		_coapServer.start();
	}
	
	/**
	 * Stop a COAP server
	 */
	public void stop() {
		_coapServer.stop();
	}
}
