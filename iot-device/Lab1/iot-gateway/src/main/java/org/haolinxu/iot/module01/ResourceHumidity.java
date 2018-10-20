/**
 * 
 */
package org.haolinxu.iot.module01;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.server.resources.CoapExchange;

/**
 * @author Alex
 *
 */
public class ResourceHumidity extends CoapResource {

	private static final Logger _Logger = 
			Logger.getLogger(ResourceHumidity.class.getName());
	
	
	
	/**
	 * @param name
	 */
	public ResourceHumidity(String name) {
		super(name);
	}

	/**
	 * @param name
	 * @param visible
	 */
	public ResourceHumidity(String name, boolean visible) {
		super(name, visible);
	}
	
	public void handleGET(CoapExchange ce) {
		
		String responseMsg = "Hers's my response to: " + super.getName();
		
		// ***
		ce.respond(ResponseCode.VALID,responseMsg);
		// ***
		
		_Logger.info("Handling GET: " + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
		
	}
	
	
	

}
