package antikythera.history;

import antikythera.time.TimeSpecification;

/**
 * Created by Nick on 1/14/14.
 */
public abstract class DataRequest {
    public abstract TickType getTickType();
    public abstract TimeSpecification getTimeSpecification();

    public enum TickType {Tick, OneMin, FiveMin, ThirtyMin, Hourly, Daily, Weekly}
}
