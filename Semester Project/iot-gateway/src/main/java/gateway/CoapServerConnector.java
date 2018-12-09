package gateway;

import java.util.logging.Logger;
import org.eclipse.californium.core.CoapServer;

public class CoapServerConnector {	
	// static
	private static final Logger _Logger = Logger.getLogger(CoapServerConnector.class.getName());
	// private var's
	private CoapServer _coapServer;
	

	// constructors
	/**
	 * Default.
	 *
	 */
	public CoapServerConnector() {
		super();
	}

	public void start() {

		_Logger.info("Creating CoAP server instance and 'temp' handler...");

		_coapServer = new CoapServer();
		

		TempResourceHandler tempHandler = new TempResourceHandler("temp");

		_coapServer.add(tempHandler);
		
		_coapServer.start();
		
	}

	public void stop() {
		_Logger.info("Stopping CoAP server...");
		_coapServer.stop();
	}
}
