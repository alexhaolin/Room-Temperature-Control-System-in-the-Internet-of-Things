package org.haolinxu.iot.module07;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.server.resources.CoapExchange;

public class TempResourceHandler extends CoapResource{

	private static final Logger _Logger = Logger.getLogger(TempResourceHandler.class.getName());
	
	public TempResourceHandler() {
		super("temp",true);
	}
	
	public TempResourceHandler(String name) {
		super(name);
	}
	
	@Override
	public void handleGET(CoapExchange ce) {
		String resmsg = "Response to: " + super.getName();
		ce.respond(ResponseCode.VALID,resmsg);
		System.out.println("Received response from the client.");
		
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	public void handlePOST(CoapExchange ce) {
		String resmsg = "Response to: " + super.getName();
		ce.respond(ResponseCode.VALID,resmsg);
		System.out.println("Received response from the client.");
		ce.accept();
		
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	public void handleDELETE(CoapExchange ce) {
		String resmsg = "Response to: " + super.getName();
		ce.respond(ResponseCode.VALID,resmsg);
		System.out.println("Received response from the client.");
		delete();
		
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	public void handlePUT(CoapExchange ce) {
		String resmsg = "Response to: " + super.getName();
		ce.respond(ResponseCode.VALID,resmsg);
		System.out.println("Received response from the client.");
		changed();
		
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
}
